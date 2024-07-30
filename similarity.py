import sqlite3
import ast
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_similarity_matrix():
    # Connect to the database
    conn = sqlite3.connect('communities.db')
    cursor = conn.cursor()

    # Fetch employee data
    cursor.execute('SELECT EmpID, Spaces FROM Employees')
    employees = cursor.fetchall()

    # Convert space strings to lists
    employee_spaces = {
        emp_id: ast.literal_eval(spaces) for emp_id, spaces in employees if spaces
    }
    if not employee_spaces:
        raise ValueError("No employee data found")

    # Create a list of all unique spaces
    all_spaces = set(
        space for spaces in employee_spaces.values() for space in spaces
    )
    if not all_spaces:
        raise ValueError("No spaces data found")

    # Create binary membership matrix
    emp_ids = list(employee_spaces.keys())
    space_indices = {space: idx for idx, space in enumerate(all_spaces)}

    membership_matrix = np.zeros((len(emp_ids), len(all_spaces)))

    for i, emp_id in enumerate(emp_ids):
        for space in employee_spaces[emp_id]:
            membership_matrix[i, space_indices[space]] = 1

    # Calculate similarity matrix
    similarity_matrix = cosine_similarity(membership_matrix)

    return similarity_matrix, emp_ids, employee_spaces


def recommend_spaces(
        emp_id,
        similarity_matrix,
        emp_ids,
        employee_spaces,
        top_n=3):

    emp_index = emp_ids.index(emp_id)
    similar_indices = np.argsort(-similarity_matrix[emp_index])[1:top_n+1]

    recommended_spaces = {}
    for sim_idx in similar_indices:
        sim_emp_id = emp_ids[sim_idx]
        for space in employee_spaces[sim_emp_id]:
            if space not in employee_spaces[emp_id]:
                if space not in recommended_spaces:
                    recommended_spaces[space] = similarity_matrix[emp_index][sim_idx]
                else:
                    recommended_spaces[space] += similarity_matrix[emp_index][sim_idx]

    # Sort spaces by recommendation score
    sorted_spaces = sorted(recommended_spaces.items(), key=lambda x: -x[1])
    return [space for space, score in sorted_spaces][:top_n]
