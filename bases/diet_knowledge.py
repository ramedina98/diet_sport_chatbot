# diet_knowledge.py
def get_diet_info(processed_input):
    """
    Returns relevant information about diets bases in the user input...
    """
    # Base de conocimiento simple
    diet_info = {
        "proteína": "La proteína es crucial para la recuperación muscular. Recomiendo consumir entre 1.6 y 2.2 gramos por kg de peso corporal.",
        "carbohidratos": "Los carbohidratos son esenciales para el rendimiento energético. Debes consumir carbohidratos complejos como avena, arroz integral y papas.",
        "grasas": "Las grasas saludables, como las de aguacate y frutos secos, son importantes para la función hormonal.",
        "suplementos": "Los suplementos como la creatina, proteína en polvo y BCAAs pueden ser útiles para maximizar el rendimiento deportivo.",
        "hidratos": "Hidratarse adecuadamente es clave para el rendimiento. Bebe agua regularmente durante el día."
    }

    # Search if any key word is in the kwoledge base...
    for word in processed_input:
        if word in diet_info:
            return diet_info[word]

    return None