"""Code for my project."""

def gpa_gap(current_gpa, required_gpa):
    """Calculate how much cumulative GPA is still needed."""
    if current_gpa >= required_gpa:
        return 0
    return round(required_gpa - current_gpa, 2) 

def science_gpa_gap(current_science_gpa, required_science_gpa):
    """Calculate how much science GPA is still needed."""
    if current_science_gpa >= required_science_gpa:
        return 0 
    return round(required_science_gpa - current_science_gpa, 2)

def pce_gap(current_hours, required_hours):
    """Calculate how many patient care experience hours are still needed."""

    if current_hours >= required_hours:
        return 0 
        
    return required_hours - current_hours 

def school_progress(current_gpa, current_science_gpa, current_hours, school):
    """Compare a student's current progress to one PA school's requirements."""
    return {
        "School": school["School"],
        "Cumulative GPA Gap": gpa_gap(current_gpa, school["Min_GPA"]),
        "Science GPA Gap": science_gpa_gap(
            current_science_gpa,
            school["Min_Science_GPA"]

        ),
        "PCE Hours Gap": pce_gap(
            current_hours,
            school["Required_PCE_hours"]
        )
    }

def compare_schools(current_gpa, current_science_gpa, current_hours, schools):
    """Compare a student's progress to multiple PA schools."""

    results = []

    for school in schools:
        progress = school_progress(
            current_gpa,
            current_science_gpa,
            current_hours,
            school
        )
        results.append(progress)

    return results
        