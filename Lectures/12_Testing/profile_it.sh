echo "Profiling code..."
kernprof -l $1

echo "Displaying output..."
python -m line_profiler $1.lprof
