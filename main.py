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


if __name__ == "__main__":
    print("Package examples:")
    print(f"50x50x50, 10kg: {sort(50, 50, 50, 10)}")
    print(f"160x50x50, 10kg: {sort(160, 50, 50, 10)}")
    print(f"50x50x50, 25kg: {sort(50, 50, 50, 25)}")
    print(f"160x50x50, 25kg: {sort(160, 50, 50, 25)}")
