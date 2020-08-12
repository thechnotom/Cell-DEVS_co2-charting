from Parse import Parse
import time

filename = "data/state.txt"

startTime = time.monotonic()
stateDataPoints = Parse.getCellStates(filename, [4, 42])
endTime = time.monotonic()

print("Parse complete (state.txt)")

print(f"Time taken: {endTime - startTime}s")
print(f"Number of cells: {len(stateDataPoints)}")

print()

filename = "data/output_messages.txt"

startTime = time.monotonic()
outputDataPoints = Parse.getCellStates(filename, [4, 42])
endTime = time.monotonic()

print("Parse complete (output_messages.txt)")

print(f"Time taken: {endTime - startTime}s")
print(f"Number of cells: {len(outputDataPoints)}")

print()

print(stateDataPoints[-1])
print(outputDataPoints[-1])

#for i in range(0, 100):
#    print(f"state {stateDataPoints[i]} --- output {outputDataPoints[i]}")