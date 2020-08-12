from Parse import Parse
import time

filename = "data/output_messages.txt"

startTime = time.monotonic()
outputDataPoints = Parse.getCellStates(filename, [4, 42])
endTime = time.monotonic()

print("Parse complete (output_messages.txt)")

print(f"Time taken: {endTime - startTime}s")
print(f"Number of cells: {len(outputDataPoints)}")

print()

#for i in range(0, 50):
#    print(f"output {outputDataPoints[i]}")