VueRangedatePicker.default.install(Vue)
Vue.use(VueRouter)

var cache = new Vue({
    created: function(){
        localforage.setDriver(localforage.INDEXEDDB);
    },
    methods: {
        clear: function() {
            localforage.clear();
        },
        get: function(key) {
            return localforage.getItem(key);
        },
        put: function(key, value) {
            //console.log("put", key, value);
            localforage.setItem(key, value);
            //this.cache.then( (cache) => {cache.put(new Request(key), new Response(value))});
            //this.cache[key] = value;
        },
    },
})

var mdal = new Vue({
    methods: {
        query: function(q) {
            var self = this;
            //console.log(q);
            return self.client.then( (res) => { return res.apis.MDAL.DataQuery({body: q}) })
        }
    },
    created: function() {
        var self = this;
        this.client = new SwaggerClient("/mdal.swagger.json")
        //this.clientcreated = new SwaggerClient("/mdal.swagger.json").then(function(c) {
        //    self.client = c;
        //})
        //.then(function(c) {
        //    self.client.apis.MDAL.DataQuery({body: {
        //        composition: ["temp"],
        //        aggregation: {temp: {funcs: ["COUNT"]}},
        //        variables: {temp: {
        //            name: "temp",
        //            definition: "SELECT ?t ?temp_uuid FROM ciee WHERE { ?t rdf:type brick:Temperature_Sensor . ?t bf:uuid ?temp_uuid };",
        //            },
        //        },
        //        time: {
        //            start: "2010-01-01T00:00:00-07:00",
        //            end: "2020-01-01T00:00:00-07:00",
        //            window: "3650d",
        //            aligned: true,
        //        },
        //    }}).then( (res) => {
        //        //console.log(res);
        //    });;
        //});
    },
})

var hod = new Vue({
    data:  {
        client: null,
        sites: [],
        sitemeta: {},
    },
    methods: {
        query: function(q) {
            //console.log("QUERY",q);
            return cache.get(q).then( (res) => {
                //console.log(res, res == undefined, res == null);
                if (res == undefined) {
                    return this.client.then( 
                                      (res) => { 
                                        return res.apis.HodDB.ExecuteQuery({body: {query: q}}) 
                                      }).then(
                                      (queryresult) => {
                                        return new Promise(function(resolve, reject) { cache.put(q, queryresult); return resolve(queryresult) });
                                      });
                }
                return new Promise(function(resolve, reject) { cache.put(q, res); return resolve(res) });
            });
            //return this.client.apis.HodDB.ExecuteQuery({body: {query: q}});
        },
    },
    computed: {
        percentcomplete: function() {
            return 100 * Object.keys(this.sitemeta).length / this.sites.length;
        },
    },
    created: function() {
        var self = this;
        this.client = new SwaggerClient("/hod.swagger.json");

        this.client.then(function(c) {
            // get all sites
            self.query("LIST NAMES;").then(function(res) {
                res.obj.rows.forEach(function(r) {
                    self.sites.push(r.uris[0].value);
                    return r.uris[0].value;
                });
            }).then(function() {

                // get stats for sites?
                self.sites.forEach(function(site) {
                    self.query("COUNT * FROM " + site + " WHERE { ?x rdf:type ?y };").then((res) => {
                        //self.$set(self.sitemeta, site, {'entities': res.obj.count})
                        //cache.put("COUNT * FROM " + site + " WHERE { ?x rdf:type ?y };", res);
                        var meta = {'entities': res.obj.count};
                        return meta;
                    }).then( (meta) => {
                        self.query("LIST VERSIONS FOR " + site + ";").then( (res) => {
                            //cache.put("LIST VERSIONS FOR " + site + ";", res);
                            if (res.obj.rows != null) {
                                meta['versions'] = res.obj.rows.map(function(r) {
                                    return r.uris[1].value;
                                });
                                meta['numversions'] = meta['versions'].length;
                            }
                            return meta;
                        }).then( (r) => {
                            self.query("SELECT ?prop ?value FROM " + site + " WHERE { ?s rdf:type brick:Site . ?s ?prop ?value };").then( (res) => {
                                //cache.put("SELECT ?prop ?value FROM " + site + " WHERE { ?s rdf:type brick:Site . ?s ?prop ?value };", res);
                                if (res.obj.rows != null) {
                                    res.obj.rows.forEach(function(r) {
                                        if ((r.uris[0].value != 'isSiteOf')) {
                                            meta[r.uris[0].value] = r.uris[1].value;
                                        }
                                    });
                                }
                                self.$set(self.sitemeta, site, meta);
                            });
                            self.$set(self.sitemeta, site, meta);
                        })
                    });
                });

            }).then(function() {
                self.sites.forEach(function(site) {
                });
            });

        });
    },
})

const Home = {
    template: '\
        <div>\
            <v-layout row wrap>\
                <v-flex xs6>\
                    <h1 class="text-xs-left display-4 font-weight-bold">MORTAR</h1>\
                    <h3 class="text-xs-left display-1">Modular Open Reproducibility Testbed for Analysis and Research</h3>\
                    <p class="py-5 text-xs-left body-2">\
                        Access to large amounts of real-world data has long been a barrier to the development and evaluation of analytics applications for the built environment.\
                        Open data sets exist, but they are limited in their span (how much data is available) and context (what kind of data is available and how it is described).\
                        Evaluation of such analytics is also limited by how the analytics themselves are implemented, often using hard-coded names of building components, points and locations, or unique input data formats.\
                    </p>\
                </v-flex>\
            </v-layout>\
        </div>\
    ',
}

const Browse = {
    data: function() {
            return {
                search: '',
                headers:[
                    {text: 'Site Name', align: 'left', sortable: true, value: 'site'},
                    {text: 'Explore', align: 'center', sortable: false, value: 'vizlink', width: "20px"},
                    {text: 'Equipment', align: 'center', sortable: false, value: 'equiplink', width: "20px"},
                    {text: 'Sq Feet', align: 'left', sortable: true, value: 'AreaSquareFeet'},
                    {text: 'Country', align: 'left', sortable: true, value: 'Country'},
                    {text: 'NumFloors', align: 'left', sortable: true, value: 'NumFloors'},
                    {text: 'Timezone', align: 'left', sortable: true, value: 'Timezone'},
                    {text: 'ZipCode', align: 'left', sortable: true, value: 'ZipCode'},
                    {text: '# Versions', align: 'left', sortable: true, value: 'numversions'},
                    {text: '# Entities', align: 'left', sortable: true, value: 'entities'},
                ]
            }
        },
    computed: {
        sites: function() {
            return hod.sites;
        },
        sitemeta: function() {
            return hod.sitemeta;
        },
        siteLoadProgress: function() {
            return hod.percentcomplete;
        },
        sitetabledata: function() {
            return Object.entries(hod.sitemeta).map(function(o, idx) {
                var site = o[0];
                var meta = o[1];
                return {site: site,
                        vizlink: '/view/'+site,
                        equiplink: '/equip/'+site+'/list',
                        AreaSquareFeet: meta.AreaSquareFeet ? meta.AreaSquareFeet : 'n/a',
                        Country: meta.Country ? meta.Country : 'n/a',
                        NumFloors: meta.NumFloors ? meta.NumFloors : 'n/a',
                        Timezone: meta.Timezone ? meta.Timezone : 'n/a',
                        ZipCode: meta.ZipCode ? meta.ZipCode : 'n/a',
                        numversions: meta.numversions,
                        entities: meta.entities}
            })
        },
        pageitems: function() {
            // use this to display 20 items by default
            return [20, {"text":"all","value":-1}]
        }
    },
    template: '\
        <div>\
            <h2 class="text-xs-left display-1 font-weight-bold py-3">Site Browser</h2>\
            <v-progress-linear v-if="this.siteLoadProgress < 100" color="info" height="10" :value="this.siteLoadProgress"></v-progress-linear>\
            <template>\
                <v-card>\
                    <v-card-title>\
                        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>\
                    </v-card-title>\
                    <v-data-table :search="search" :headers="this.headers" :items="this.sitetabledata" class="elevation-1" :rows-per-page-items="this.pageitems">\
                        <template slot="items" slot-scope="props">\
                            <td>{{ props.item.site }}</td>\
                            <td class="text-xs-center"><router-link :to="props.item.vizlink"><v-icon>fa-arrow-circle-right</v-icon></router-link></td>\
                            <td class="text-xs-center"><router-link :to="props.item.equiplink"><v-icon>fa-arrow-circle-right</v-icon></router-link></td>\
                            <td>{{ props.item.AreaSquareFeet }}</td>\
                            <td>{{ props.item.Country }}</td>\
                            <td>{{ props.item.NumFloors }}</td>\
                            <td>{{ props.item.Timezone }}</td>\
                            <td>{{ props.item.ZipCode }}</td>\
                            <td>{{ props.item.numversions }}</td>\
                            <td>{{ props.item.entities }}</td>\
                        </template>\
                        <v-alert slot="no-results" :value="true" color="error" icon="warning">\
                            Your search for "{{ search }}" found no results.\
                        </v-alert>\
                    </v-data-table>\
                </v-card>\
            </template>\
        </div>\
    ',
}

const EquipmentList = {
    props: ['site'],
    mounted: function() {
        var self = this;
        var q = "SELECT ?equiptype ?equip FROM " + this.site + " WHERE { ?equip rdf:type/rdfs:subClassOf* brick:Equipment . ?equip rdf:type ?equiptype };";
        hod.query("SELECT ?equiptype ?equip FROM " + this.site + " WHERE { ?equip rdf:type/rdfs:subClassOf* brick:Equipment . ?equip rdf:type ?equiptype };").then( (res) => {
            //cache.put(q, res);
            res.obj.rows.forEach(function(r) {
                var type = r.uris[0].value;
                var name = r.uris[1].value;
                if (self.equiptypes[type] == null) {
                    self.$set(self.equiptypes, type, [])
					self.count += 1;
                }
                self.equiptypes[type].push(name)
            })
        })
    },
    data: function() {
        return {
            equiptypes: {},
            clicked: [],
			count: 0,
        }
    },
    methods: {
        dig: function(equipname) {
            this.clicked.push(equipname)
            router.push("/equip/"+this.site+"/list/"+equipname);
        },
    },
    template: '\
        <div>\
            <template>\
			<v-layout row>\
			<v-flex xs12 sm6 offset-sm3>\
			<v-card> \
                <v-list>\
                    <template v-for="(equiplist, equipname, index) in this.equiptypes">\
                        <v-list-tile :key="equipname" avatar ripple @click="dig(equipname)">\
                            <v-list-tile-content color="grey lighten-3">\
                                <v-list-tile-title>{{ equipname }}</v-list-tile-title>\
                                <v-list-tile-sub-title class="text--primary">{{ equiplist.length }} found</v-list-tile-sub-title>\
                            </v-list-tile-content>\
							<v-list-tile-action>\
							  <v-list-tile-action-text>List</v-list-tile-action-text>\
							  <v-icon color="blue darken-2">search</v-icon>\
							</v-list-tile-action>\
                        </v-list-tile>\
						<v-divider v-if="index + 1 < count" :key="index"></v-divider>\
                    </template>\
                </v-list>\
			</v-card>\
			</v-flex>\
			</v-layout>\
            </template>\
        </div>\
    '
}

const EquipmentView = {
    props: ['site', 'classname'],
    data: function() {
        var rows = [];
        var self = this;
        hod.query("SELECT ?equip ?point ?uuid ?equiptype ?pointtype FROM " + this.site + " WHERE { ?equip bf:hasPoint ?point . ?point bf:uuid ?uuid . ?equip rdf:type ?equiptype . ?point rdf:type ?pointtype};").then( (res) => {
            res.obj.rows.forEach(function(r) {
                if (self.classname != null && r.uris[3].value == self.classname) {
                    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value});
                }
                if (self.classname == null || (self.classname != null && r.uris[3].value == self.classname)) {
                    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value, 'equipgraphlink': "/point/"+self.site+"/"+r.uris[3].value});
                }
            })
        })
        return {
            rows: rows,
            search: '',
            selected: [],
            headers:[
                {text: 'Equipment', align: 'left', sortable: true, value: 'equip'},
                {text: 'Equipment Type', align: 'left', sortable: true, value: 'equiptype'},
                {text: 'Point', align: 'left', sortable: true, value: 'point'},
                {text: 'Point Type', align: 'left', sortable: true, value: 'pointtype'},
                {text: 'UUID', align: 'left', sortable: true, value: 'uuid'},
            ]
        }
    },
    computed: {
        pageitems: function() {
            // use this to display 20 items by default
            return [20, {"text":"all","value":-1}]
        },
        equiplink: function() {
            return "/equip/"+this.site+"/list"
        },
        plotlink: function() {
            return "/plot/"+this.selected.map(function(e) { return e['uuid']}).join(",");
        },
    },
    beforeRouteUpdate: function (to, from, next) {
        this.classname = null;
        var rows = [];
        var self = this;
        hod.query("SELECT ?equip ?point ?uuid ?equiptype ?pointtype FROM " + this.site + " WHERE { ?equip bf:hasPoint ?point . ?point bf:uuid ?uuid . ?equip rdf:type ?equiptype . ?point rdf:type ?pointtype};").then( (res) => {
            res.obj.rows.forEach(function(r) {
                if (self.classname == null || (self.classname != null && r.uris[3].value == self.classname)) {
                    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value, 'equipgraphlink': "/point/"+self.site+"/"+r.uris[3].value});
                }
            })
            self.rows = rows;
            next(); // next route
        })
    },
    template: '\
        <div>\
            <h2 class="text-xs-left display-1 font-weight-bold py-3"><b>{{ site }}</b> - Equipment Browser <span v-if="this.classname != null"> - {{ classname }}</span></h2>\
            <template>\
                <v-card>\
                    <v-card-title>\
                        <v-btn color="success" :disabled="this.selected.length == 0" v-bind:to="this.plotlink">Plot Selected</router-link></v-btn>\
                        <v-btn color="info" v-if="this.classname != null" v-bind:to="this.equiplink">All</router-link></v-btn>\
                        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>\
                    </v-card-title>\
                    <v-data-table :headers="this.headers" :items="this.rows" v-model="selected" item-key="uuid" select-all :search="search" lass="elevation-1" :rows-per-page-items="this.pageitems">\
                        <template slot="headerCell" slot-scope="props">\
                            <v-tooltip bottom>\
                                <span slot="activator">{{ props.header.text }}</span>\
                                <span>{{ props.header.text }}</span>\
                            </v-tooltip>\
                        </template>\
                        <template slot="items" slot-scope="props">\
                            <td><v-checkbox v-model="props.selected" primary hide-details></v-checkbox></td>\
                            <td>{{ props.item.equip }}</td>\
                            <td>{{ props.item.equiptype }}</td>\
                            <td>{{ props.item.point }}</td>\
                            <td><router-link :to="`/point/${site}/${props.item.pointtype}`">{{ props.item.pointtype }}</router-link></td>\
                            <td>{{ props.item.uuid }}</td>\
                        </template>\
                        <v-alert slot="no-results" :value="true" color="error" icon="warning">\
                            Your search for "{{ search }}" found no results.\
                        </v-alert>\
                        <v-alert slot="no-data" :value="true" color="error" icon="warning">\
                            Equipment of type "brick:{{ this.classname }}" has no points\
                        </v-alert>\
                    </v-data-table>\
                </v-card>\
            </template>\
        </div>\
    ',
}

const EquipmentViewWithPlot = {
    props: ['site', 'classname'],
    data: function() {
        var rows = [];
        var self = this;
        hod.query("SELECT ?equip ?point ?uuid ?equiptype ?pointtype FROM " + this.site + " WHERE { ?equip bf:hasPoint ?point . ?point bf:uuid ?uuid . ?equip rdf:type ?equiptype . ?point rdf:type ?pointtype};").then( (res) => {
            res.obj.rows.forEach(function(r) {
                //if (self.classname != null && r.uris[3].value == self.classname) {
                //    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value});
                //}
                if (self.classname == null || (self.classname != null && r.uris[3].value == self.classname)) {
                    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value, 'equipgraphlink': "/point/"+self.site+"/"+r.uris[3].value});
                }
            })
            self.fetchData();
        })
        return {
            rows: rows,
            search: '',
            selected: [],
            uuids: [],
            start: new Date(),
            end: dateFns.addDays(new Date(), -365),
            loadingData: false,
            hasdata: false,
            minDate: null,
            maxDate: null,
            widths: [{text: "365d"},
                     {text: "30d"},
                     {text: "7d"},
                     {text: "1d"},
                     {text: "1h"}],
            headers:[
                {text: 'Equipment', align: 'left', sortable: true, value: 'equip'},
                {text: 'Equipment Type', align: 'left', sortable: true, value: 'equiptype'},
                {text: 'Point', align: 'left', sortable: true, value: 'point'},
                {text: 'Point Type', align: 'left', sortable: true, value: 'pointtype'},
                {text: 'UUID', align: 'left', sortable: true, value: 'uuid'},
            ]
        }
    },
    methods:  {
        contextForUUID: function(uuid) {
            return hod.query('SELECT ?name ?class FROM ' + this.site + ' WHERE { ?name rdf:type ?class . ?name bf:uuid "'+uuid+'" };')
        },
        getResolution: function(hours) {
            if (hours <= 1 ) {
                return '1m';
            } else if (hours <= 24) {
                return '10m';
            } else if (hours <= 24 * 7) {
                return '1h';
            } else if (hours <= 24 * 34) {
                return '1h';
            } else {
                return '1d';
            }
        },
        plot: function(data, labels) {
            var self = this;
            self.loadingData = false;
            if (data.length == 0) { return }
            new Dygraph(document.getElementById("vizdivuuid"),
                data,
                {
                    labels: labels,
                    width: "100%",
                    height: 300,
                    labelsDiv: "vizdivlegend",
                    labelsSeparateLines: true,
                    legend: "always",
                    zoomCallback: function(minDate, maxDate, yRange) {
                        console.log(minDate, maxDate, yRange, minDate==self.minDate, maxDate==self.maxDate);
                        if (maxDate == self.maxDate || minDate == self.minDate) {
                            return;
                        }
                        self.start = maxDate;
                        self.end = minDate;
                        self.maxDate = maxDate;
                        self.minDate = minDate;
                        self.fetchData();
                        //var hours = (maxDate - minDate) / (1000*60*60);
                        //console.log("HOURS", hours);
                        //con
                    },
                }
            );
        },
        adjustDay: function(amount) {
            this.start = dateFns.addDays(this.start, amount);
            this.end = dateFns.addDays(this.end, amount);
            this.fetchData();
        },
        onDateSelected: function(chosen) {
            this.start = chosen.end;
            this.end = chosen.start;
            this.fetchData();
        },
        fetchData: function() {
            var self = this;
            self.loadingData = true;
            console.log(dateFns.format(self.start, "YYYY-MM-DDTHH:mm:ssZ'"));
            var hours = dateFns.differenceInHours(self.start, self.end)
            console.log("HOURS",hours);
            var q = {
                composition: ["data"],
                aggregation: {data: {funcs: ["MEAN"]}},
                variables: {data: {
                    name: "data",
                    uuids: self.selected.map(function(e) { return e['uuid']}),
                    definition: "SELECT ?t ?temp_uuid FROM " + self.site + " WHERE { ?t rdf:type brick:" + self.class + " . ?t bf:uuid ?temp_uuid };", // this gets ignored
                    },
                },
                time: {
                    start:self.startf,
                    end:self.endf,
                    window: self.getResolution(hours),
                    aligned: true,
                },
            };
            console.log(q);
            mdal.query(q).then( (res) => {
                var data = [];
                //cache.put(q, res);
                console.log(res);
                self.hasdata = (res.obj.result.uuids != null);
                if (res.obj.result.error != null) {
                    console.error(res.obj.result.error);
                    data = [];
                    self.plot(data, labels);
                    return;
                } else {
                    var labels = ["time"];
                    var uuidlabels = res.obj.result.uuids.map(function(uuid) {
                        return self.contextForUUID(uuid);
                    });
                    Promise.all(uuidlabels).then(values => {
                        console.log(values);
                        values.forEach(v => {
                            //console.log(v);
                            labels.push(v.obj.rows[0].uris[0].value);
                        });
                        for (i=0;i<res.obj.result.times.length;i++) {
                            var tmp = [new Date(res.obj.result.times[i] / 1000000)];
                            res.obj.result.values.forEach(function(e) {
                                if (!isNaN(e.value[i])) {
                                    tmp.push(e.value[i]);
                                } else {
                                    tmp.push(null);
                                }
                            });
                            data.push(tmp);
                        }
                        self.plot(data, labels);
                        return;
                    });

                }
            });
        },
    },
    mounted: function() {
        this.fetchData();
    },
    computed: {
        startf : function() {
            return dateFns.format(this.start, "YYYY-MM-DDTHH:mm:ssZ");
        },
        endf : function() {
            return dateFns.format(this.end, "YYYY-MM-DDTHH:mm:ssZ");
        },
        pageitems: function() {
            // use this to display 20 items by default
            return [20, {"text":"all","value":-1}]
        },
        equiplink: function() {
            return "/equip/"+this.site+"/list"
        },
        plotlink: function() {
            return "/plot/"+this.selected.map(function(e) { return e['uuid']}).join(",");
        },
    },
    beforeRouteUpdate: function (to, from, next) {
        this.classname = null;
        var rows = [];
        var self = this;
        hod.query("SELECT ?equip ?point ?uuid ?equiptype ?pointtype FROM " + this.site + " WHERE { ?equip bf:hasPoint ?point . ?point bf:uuid ?uuid . ?equip rdf:type ?equiptype . ?point rdf:type ?pointtype};").then( (res) => {
            res.obj.rows.forEach(function(r) {
                if (self.classname == null || (self.classname != null && r.uris[3].value == self.classname)) {
                    rows.push({'equip': r.uris[0].value, 'point': r.uris[1].value, 'uuid': r.uris[2].value, 'equiptype': r.uris[3].value, 'pointtype': r.uris[4].value, 'equipgraphlink': "/point/"+self.site+"/"+r.uris[3].value});
                }
            })
            self.rows = rows;
            next(); // next route
        })
    },
    template: '\
        <div>\
            <h2 class="text-xs-left display-1 font-weight-bold py-3"><b>{{ site }}</b> - Equipment Browser <span v-if="this.classname != null"> - {{ classname }}</span></h2>\
            <v-progress-linear v-if="loadingData" :indeterminate="true"></v-progress-linear>\
            <div id="vizdiv">\
                <v-layout row wrap>\
                    <v-flex xs12>\
                        <v-alert :value="!hasdata" type="error">No data found in the given time range</v-alert>\
                    </v-flex>\
                </v-layout>\
                <v-layout row wrap>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-365)">-1y</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-30)">-1month</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-7)">-1week</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-1)">-1day</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(1)">+1day</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(7)">+1week</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(30)">+1month</v-btn>\
                    <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(365)">+1year</v-btn>\
                    <v-overflow-btn :items="widths" label="Width" editable item-value="text" overflow></v-overflow-btn>\
                    <div class="daterange-wrapper"><vue-rangedate-picker @selected="onDateSelected" i18n="EN"></vue-rangedate-picker></div>\
                </v-layout>\
                <v-layout row wrap>\
                    <v-flex xs10>\
                        <div id="vizdivuuid"></div>\
                    </v-flex>\
                    <v-flex xs2>\
                        <span id="vizdivlegend"></span>\
                    </v-flex>\
                </v-layout>\
            </div>\
            <template>\
                <v-card>\
                    <v-card-title>\
                        <v-btn color="success" :disabled="this.selected.length == 0" v-on:click="this.fetchData">Plot Selected</router-link></v-btn>\
                        <v-btn color="info" v-if="this.classname != null" v-bind:to="this.equiplink">All</router-link></v-btn>\
                        <v-text-field v-model="search" append-icon="search" label="Search" single-line hide-details></v-text-field>\
                    </v-card-title>\
                    <v-data-table :headers="this.headers" :items="this.rows" v-model="selected" item-key="uuid" select-all :search="search" lass="elevation-1" :rows-per-page-items="this.pageitems">\
                        <template slot="headerCell" slot-scope="props">\
                            <v-tooltip bottom>\
                                <span slot="activator">{{ props.header.text }}</span>\
                                <span>{{ props.header.text }}</span>\
                            </v-tooltip>\
                        </template>\
                        <template slot="items" slot-scope="props">\
                            <td><v-checkbox v-model="props.selected" primary hide-details></v-checkbox></td>\
                            <td>{{ props.item.equip }}</td>\
                            <td>{{ props.item.equiptype }}</td>\
                            <td>{{ props.item.point }}</td>\
                            <td><router-link :to="`/point/${site}/${props.item.pointtype}`">{{ props.item.pointtype }}</router-link></td>\
                            <td>{{ props.item.uuid }}</td>\
                        </template>\
                        <v-alert slot="no-results" :value="true" color="error" icon="warning">\
                            Your search for "{{ search }}" found no results.\
                        </v-alert>\
                        <v-alert slot="no-data" :value="true" color="error" icon="warning">\
                            Equipment of type "brick:{{ this.classname }}" has no points\
                        </v-alert>\
                    </v-data-table>\
                </v-card>\
            </template>\
        </div>\
    ',
}

const View = {
    props: ['site'],
    data: function() {
        return {
            nodes: [],
            links: [],
            svg: null,
            selected: [],
            tablelink: '',
        }
    },
    mounted: function() {
		var svg = d3.select("svg"),
			width = +svg.attr("width"),
			height = +svg.attr("height");
        this.svg = svg;

		this.color = d3.scaleOrdinal(d3.schemeCategory20);

		var simulation = d3.forceSimulation()
			.force("link", d3.forceLink().id(function(d) { return d.id; }).distance(150).strength(0.1))
			.force("charge", d3.forceManyBody().strength(-500))
			.force("center", d3.forceCenter(width / 2, height / 2));
        this.simulation = simulation

        var self = this;
        this.dragstarted = function(d) {
		  if (!d3.event.active) self.simulation.alphaTarget(0.3).restart();
		  d.fx = d.x;
		  d.fy = d.y;
		}
		this.dragged = function(d) {
		  d.fx = d3.event.x;
		  d.fy = d3.event.y;
		}

		this.dragended = function(d) {
		  if (!d3.event.active) self.simulation.alphaTarget(0);
		  d.fx = null;
		  d.fy = null;
		}


        // always node edge node
        this.renderquery("SELECT ?class ?pred ?otherclass FROM " + this.site + " WHERE { ?x rdf:type ?class . ?x ?pred ?object . ?object rdf:type ?otherclass . ?x rdf:type brick:Room };");
    },
    methods: {
        renderbrickclass: function(c) {
            this.renderquery("SELECT ?class ?pred ?otherclass FROM " + this.site + " WHERE { ?x rdf:type ?class . ?x ?pred ?object . ?object rdf:type ?otherclass . ?x rdf:type brick:" + c + " };");
        },
        ticked: function(node, link, edgepaths, edgelabels) {
            node
                .attr("transform", function(d) {
                  return "translate(" + d.x + "," + d.y + ")";
                })
            link
                .attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; });
            edgepaths
                .attr('d', function (d) {
                    return 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y;
                });
            edgelabels
                .attr('transform', function (d) {
                    if (d.target.x < d.source.x) {
                        var bbox = this.getBBox();
                        rx = bbox.x + bbox.width / 2;
                        ry = bbox.y + bbox.height / 2;
                        return 'rotate(180 ' + rx + ' ' + ry + ')';
                    }
                    else {
                        return 'rotate(0)';
                    }
            });
        },
        renderquery: function(q) {
            var self = this;
            hod.query(q).then( (queryresult) => {
                queryresult.obj.rows.forEach(function(r) {
                    // filter query results
                    var name = r.uris[0].value;
                    if (name == 'Class' || name == 'Site'|| name.indexOf('Property') >= 0 || name.indexOf('Ontology') >= 0 ) {
                        return true;
                    }
                    var name = r.uris[2].value;
                    if (name == 'Class' || name == 'Site'|| name.indexOf('Property') >= 0 || name.indexOf('Ontology') >= 0 ) {
                        return true;
                    }

                    // add new nodes to the graph if they don't already exist
                    if (!self.nodes.find(function(n) { return n.id == r.uris[0].value})) {
                        //console.log('adding', r.uris[0].value);
                        self.nodes.push({"id": r.uris[0].value});
                    }
                    if (!self.nodes.find(function(n) { return n.id == r.uris[2].value})) {
                        //console.log('adding', r.uris[2].value);
                        self.nodes.push({"id": r.uris[2].value});
                    }

                    // add new links
                    if (!self.links.find(function(l) {
                        return ( (l.source.id == r.uris[0].value && l.target.id == r.uris[2].value && l.value.id == r.uris[1].value) || (l.target.id == r.uris[0].value && l.source.id == r.uris[2].value) );
                    })) {
                        //console.log('add new link?', r.uris);
                        self.links.push({"source": r.uris[0].value, "target":r.uris[2].value, "value": r.uris[1].value});
                    }
                });
            }).then( () => {
                // update the node attributes
                d3.selectAll("svg > *").remove();
                self.simulation.alphaTarget(0)
                self.svg.append('defs').append('marker')
                    .attr('id','arrowhead',)
                    .attr('viewBox','-0 -5 10 10')
                    .attr('refX',20)
                    .attr('refY',0)
                    .attr('orient','auto')
                    .attr('markerWidth',13)
                    .attr('markerHeight',13)
                    .attr('xoverflow','visible')
                    .append('svg:path')
                    .attr('d', 'M 0,-3 L 8 ,0 L 0,3')
                    .attr('fill', '#999')
                    .style('stroke','none');
                // update the link attributes
                self.link = self.svg.append("g")
                      .attr("class", "links")
                      .attr('marker-end','url(#arrowhead)')
                    .selectAll("line")
                    .data(self.links)
                    .enter().append("line")
                      .attr("stroke-width", 2);
                var linklabel = self.link.append("text")
                  .text(function(n) { return n.value; })
                  .attr('x', 20)
                  .attr('y', 20);
                self.node = self.svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("g")
                    .data(self.nodes)
                    .enter().append("g");
			    self.circles = self.node.append("circle")
			  	    .attr("r", 30)
			  	    .attr("fill", function(d) { return d.color == null ? self.color(1) : self.color(10); })
			  	    .call(d3.drag()
			  		  .on("start", self.dragstarted)
			  		  .on("drag", self.dragged)
			  		  .on("end", self.dragended))
                    .on("click", function(n) {
                      n.color = 10;
                      self.selected.push(n.id);
                      console.log(self.selected);
                      self.renderbrickclass(n.id)
                    });
                  var edgepaths = self.svg.append('g').attr('class','edgepath').selectAll('.edgepath').data(self.links)
                                        .enter().append('path')
                                        .attr('class','edgepath')
                                        .attr('fill-opacity', 0)
                                        .attr('stroke-opacity', 0)
                                        .attr('id', function(d, i) { return 'edgepath'+i });
                  var edgelabels = self.svg.append('g').attr('class','edgelabel').selectAll('.edgelabel').data(self.links)
                                        .enter().append('text')
                                            .style("pointer-events", "none")
                                            .attr('class', 'edgelabel')
                                            .attr('id', function(d, i) { return 'edgelabel' + i })
                                            .attr('font-size', 10)
                                            .attr('fill', '#aaa');

                    edgelabels.append('textPath')
                        .attr('xlink:href', function (d, i) {return '#edgepath' + i})
                        .style("text-anchor", "middle")
                        .style("pointer-events", "none")
                        .attr("startOffset", "50%")
                        .text(function (d) {return d.value});
			    var labels = self.node.append("text")
			  	  .text(function(d) { return d.id; })
			  	  .attr('x', 32)
			  	  .attr('y', 0);

                self.simulation
                    .nodes(self.nodes)
                    .on("tick", function() { self.ticked(self.node, self.link, edgepaths, edgelabels)} );
                self.simulation.force("link")
                    .links(self.links);
                self.simulation.alphaTarget(0.3).restart()
            })
        },
    },
	template: '\
		<div>\
		<svg width=1200 height=900></svg>\
		</div>\
    '
}

Vue.component('navigation', {
    computed: {
        nothome: function() {
            return $route.name == 'home';
        },
    },
    template: '\
        <v-navigation-drawer app permanent v-if="true">\
            <v-toolbar flat>\
                <v-list>\
                    <v-list-tile>\
                        <v-list-tile-title class="title">\
                            <router-link to="/" class="menumortartitle">Mortar</router-link>\
                        </v-list-tile-title>\
                    </v-list-tile>\
                </v-list>\
            </v-toolbar>\
            <v-divider></v-divider>\
            <v-list>\
             <v-list-tile to="/browse">\
                <v-list-tile-content>\
                  <v-list-tile-title><router-link to="/browse" class="menumortartitle">Site List</router-link></v-list-tile-title>\
                </v-list-tile-content>\
              </v-list-tile>\
        </v-navigation-drawer>\
    '
})

const TimeViz = {
    props: ["class", "site"],
    data: function() {
        return {
             start: new Date(),
             end: dateFns.addDays(new Date(), -7),
             hasdata: false,
             widths: [{text: "365d"},
                      {text: "30d"},
                      {text: "7d"},
                      {text: "1d"},
                      {text: "1h"}],
        }
    },
    computed: {
        startf : function() {
            return dateFns.format(this.start, "YYYY-MM-DDTHH:mm:ssZ");
        },
        endf : function() {
            return dateFns.format(this.end, "YYYY-MM-DDTHH:mm:ssZ");
        },
    },
    methods: {
        adjustDay: function(amount) {
            this.start = dateFns.addDays(this.start, amount);
            this.end = dateFns.addDays(this.end, amount);
            this.plotTime();
        },
        plotTime: function() {
            var self = this;

            console.log(this.startf, this.endf);
            mdal.query({
                composition: ["data"],
                aggregation: {data: {funcs: ["MEAN"]}},
                variables: {data: {
                    name: "data",
                    definition: "SELECT ?t ?temp_uuid FROM " + this.site + " WHERE { ?t rdf:type brick:" + this.class + " . ?t bf:uuid ?temp_uuid };",
                    },
                },
                time: {
                    start: self.startf,
                    end: self.endf,
                    window: "1h",
                    aligned: true,
                },
            }).then( (res) => {
                var data = [];
                var labels = ["time"];
                var hasData = (res.obj.result.context != null);
                if (hasData) {
                    res.obj.result.context.forEach(function(l) {
                        labels.push(l.row['?t'].split('#')[1]);
                    });

                    for (i=0;i<res.obj.result.times.length;i++) {
                        var tmp = [new Date(res.obj.result.times[i] / 1000000)];
                        res.obj.result.values.forEach(function(e) {
                            if (!isNaN(e.value[i])) {
                                tmp.push(e.value[i]);
                            } else {
                                tmp.push(null);
                            }
                        });
                        data.push(tmp);
                    }
                    new Dygraph(document.getElementById("vizdivuuid"),
                        data,
                        {
                            labels: labels,
                            width: "100%",
                            height: 500,
                            labelsDiv: "vizdivlegend",
                            labelsSeparateLines: true,
                            legend: "always",
                        }
                    );
                    self.hasdata = true;
                } else {
                    self.hasdata = false;
                }
            });
        },
    },
    mounted: function() {
        this.plotTime();
    },
    template: '\
        <div id="vizdiv">\
            <v-layout row wrap>\
                <v-flex xs12>\
                    <v-alert :value="!hasdata" type="error">No data found in the given time range</v-alert>\
                </v-flex>\
            </v-layout>\
            <v-layout row wrap>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-365)">-1y</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-30)">-1month</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-7)">-1week</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(-1)">-1day</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(1)">+1day</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(7)">+1week</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(30)">+1month</v-btn>\
                <v-btn small color="blue-grey" class="white--text" v-on:click="adjustDay(365)">+1year</v-btn>\
                <v-overflow-btn :items="widths" label="Width" editable item-value="text" overflow></v-overflow-btn>\
            </v-layout>\
            <div id="vizdivuuid"></div>\
            <div id="vizdivlegend"></div>\
        </div>\
    '
}

const PlotViz = {
    props: ["uuids"],
    data: function() {
        return {
             start: new Date(2018, 7, 1, 0,0,0),
             end: new Date(2018, 9, 1, 0,0,0),
        }
    },
    methods:  {
    },
    mounted: function() {
        var self = this;
        console.log(dateFns.format(this.start, "YYYY-MM-DDTHH:mm:ssZ'"));
        mdal.query({
            composition: ["data"],
            aggregation: {data: {funcs: ["MEAN"]}},
            variables: {data: {
                name: "data",
                uuids: self.uuids.split(','),
                definition: "SELECT ?t ?temp_uuid FROM " + this.site + " WHERE { ?t rdf:type brick:" + this.class + " . ?t bf:uuid ?temp_uuid };",
                },
            },
            time: {
                start:self.startf,
                end:self.endf,
                window: "1h",
                aligned: true,
            },
        }).then( (res) => {
            var data = [];
            console.log(res);
            var labels = ["time"];
            res.obj.result.context.forEach(function(l) {
                labels.push(l.uuid); //.row['?t'].split('#')[1]);
            });

            for (i=0;i<res.obj.result.times.length;i++) {
                var tmp = [new Date(res.obj.result.times[i] / 1000000)];
                res.obj.result.values.forEach(function(e) {
                    if (!isNaN(e.value[i])) {
                        tmp.push(e.value[i]);
                    } else {
                        tmp.push(null);
                    }
                });
                data.push(tmp);
            }
            new Dygraph(document.getElementById("vizdivuuid"),
                data,
                {
                    labels: labels,
                    width: "100%",
                    height: 500,
                    labelsDiv: "vizdivlegend",
                    labelsSeparateLines: true,
                }
            );
        });

    },
    template: '\
        <div>\
            <div id="vizdivuuid"></div>\
            <div id="vizdivlegend"></div>\
        </div>\
    '
}
const routes = [
  { path: '/', component: Home , name: 'home'},
  { path: '/browse', component: Browse, name: 'browse'},
  { path: '/view/:site', component: View, props: true, name: 'viewsite'},
  { path: '/equip/:site/list/:classname?', component: EquipmentViewWithPlot, props: true, name: 'equiplist'},
  { path: '/point/:site/:class', component: TimeViz, props: true, name: 'plotviz'},
  { path: '/plot/:uuids', component: PlotViz, props: true, name: 'pointviz'},
]

  // { path: '/equip/:site', component: EquipmentList, props: true, name: 'viewequip'},
const router = new VueRouter({
  routes // short for `routes: routes`
})


const app = new Vue({
  router,
  created: function() {
    console.log('vue mounted');
  },
  mounted: async function() {
    await mdal.clientcreated;
  },
}).$mount('#app')
