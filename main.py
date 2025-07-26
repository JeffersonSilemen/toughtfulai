def sort(width, height, length, mass) -> str:
    if width >= 150 or height >= 150 or length >= 150:
        package_type = 'bulky'
    elif (width * height * length) >= 1000000:
        package_type = 'bulky'
    elif mass >= 20:
        package_type = 'heavy'
    else:
        package_type = 'normal'
    return package_type