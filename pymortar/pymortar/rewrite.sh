for f in `ls *pb2*.py`; do
    echo $f
    sed -i -e 's/^import \([a-z_]\+_pb2\)/from pymortar import \1/' $f
done
