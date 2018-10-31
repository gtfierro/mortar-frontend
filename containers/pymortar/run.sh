cd "/home/$NB_USER"
chown -R "$NB_USER:users" .
export NOTEBOOK_FLAGS="${NOTEBOOK_FLAGS} --NotebookApp.token=\"${CONTAINER_AUTH_TOKEN}\""
#plasma_store -m 1000000000 -s /tmp/plasma &
runuser -l jovyan -c '/opt/conda/bin/plasma_store -m 1000000000 -s /tmp/plasma' & 
start-notebook.sh ${NOTEBOOK_FLAGS}
