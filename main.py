def sort(width: float, height: float, length: float, mass: float) -> str:
    package_type = []
    if width >= 150 or height >= 150 or length >= 150:
        package_type.append('bulky')
    elif (width * height * length) >= 1000000:
        package_type.append('bulky')
    if mass >= 20:
        package_type.append('heavy')

    if "bulky" in package_type and "heavy" in package_type:
        deliver = "REJECTED"
    elif "bulky" in package_type:
        deliver = "SPECIAL"
    elif "heavy" in package_type:
        deliver = "SPECIAL"
    else:
        deliver = "STANDARD"

    return deliver
