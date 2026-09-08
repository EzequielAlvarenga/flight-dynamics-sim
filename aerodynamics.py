import math

def calculate_lift_coefficient(alpha_rad, cl_alpha=2 * math.pi):
    """Calcula el coeficiente de sustentación (CL) en régimen subsónico."""
    return cl_alpha * alpha_rad
