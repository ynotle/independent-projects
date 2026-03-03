import random
import numpy as np
import math
import statistics

# --- Setup ---
startingSudoku = """
                    024007000
                    600000000
                    003680415
                    431005000
                    500000032
                    790000060
                    209710800
                    040093000
                    310004750
                """

# Convert string to clean 2D numpy array
sudoku_orig = np.array([[int(i) for i in line] for line in startingSudoku.split()])

def PrintSudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(sudoku[i, j]) + " "
        print(row_str)
    print("\n")

def GetFixedMask(sudoku):
    # Returns a boolean array where True means the number cannot be changed
    return sudoku != 0

def CalculateNumberOfErrors(sudoku):
    errors = 0
    for i in range(9):
        # Count missing unique values in rows and columns
        errors += (9 - len(np.unique(sudoku[i, :])))
        errors += (9 - len(np.unique(sudoku[:, i])))
    return errors

def CreateList3x3Blocks():
    blocks = []
    for r in range(3):
        for c in range(3):
            blockIndices = []
            for i in range(3):
                for j in range(3):
                    blockIndices.append((r * 3 + i, c * 3 + j))
            blocks.append(blockIndices)
    return blocks

def RandomlyFill3x3Blocks(sudoku, listOfBlocks):
    res = np.copy(sudoku)
    for block in listOfBlocks:
        # Get values already in this block
        vals_in_block = [res[r, c] for r, c in block if res[r, c] != 0]
        # Get values that need to be placed
        missing_vals = [v for v in range(1, 10) if v not in vals_in_block]
        random.shuffle(missing_vals)
        # Fill empty spots
        for r, c in block:
            if res[r, c] == 0:
                res[r, c] = missing_vals.pop()
    return res

def ProposedState(sudoku, fixedMask, listOfBlocks):
    new_sudoku = np.copy(sudoku)
    # Pick a random block
    block = random.choice(listOfBlocks)
    
    # Filter for boxes that are NOT fixed
    mutable_boxes = [box for box in block if not fixedMask[box[0], box[1]]]
    
    if len(mutable_boxes) < 2:
        return new_sudoku, None
    
    # Swap two random mutable boxes within the block
    b1, b2 = random.sample(mutable_boxes, 2)
    new_sudoku[b1[0], b1[1]], new_sudoku[b2[0], b2[1]] = \
        new_sudoku[b2[0], b2[1]], new_sudoku[b1[0], b1[1]]
    
    return new_sudoku, (b1, b2)

def solveSudoku(sudoku):
    fixedMask = GetFixedMask(sudoku)
    listOfBlocks = CreateList3x3Blocks()
    
    # Initial State
    currentSudoku = RandomlyFill3x3Blocks(sudoku, listOfBlocks)
    currentScore = CalculateNumberOfErrors(currentSudoku)
    
    # Cooling schedule parameters
    sigma = 1.0  # Initial temperature
    decreaseFactor = 0.999
    iterations = 1000
    
    print("Initial Board:")
    PrintSudoku(sudoku)
    
    step = 0
    while currentScore > 0:
        # Propose a change
        proposedSudoku, boxes = ProposedState(currentSudoku, fixedMask, listOfBlocks)
        if boxes is None: continue
        
        newScore = CalculateNumberOfErrors(proposedSudoku)
        scoreDiff = newScore - currentScore
        
        # Simulated Annealing Acceptance Probability
        # If scoreDiff is negative, exp(-diff/sigma) > 1, so it's always accepted
        rho = math.exp(-scoreDiff / sigma) if sigma > 0 else 0
        
        if scoreDiff < 0 or random.random() < rho:
            currentSudoku = proposedSudoku
            currentScore = newScore
        
        # Cool down
        sigma *= decreaseFactor
        step += 1
        
        if step % 5000 == 0:
            print(f"Step {step}, Errors: {currentScore}, Temp: {sigma:.4f}")
            # Re-heat logic if stuck
            if sigma < 0.01:
                sigma = 0.5 
        
        if currentScore == 0:
            print("--- Solution Found! ---")
            PrintSudoku(currentSudoku)
            return currentSudoku

solution = solveSudoku(sudoku_orig)