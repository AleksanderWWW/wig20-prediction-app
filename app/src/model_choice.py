def choose_best_from_grid(grid):
    row = grid.loc[grid['metric']==grid['metric'].min(),:]
    return row