# print("hello")
# print(5)
# print(5*20)

# usd = float(input("Enter currency in USD: "))
# inr = usd * 83.04

# print("The currency in INR is",round(inr,2))

def convert_bits_to_bytes(bits):
    bytes = bits / 8
    return bytes

def convert_bytes_to_megabytes(bytes):
    megabytes = bytes / (1024 ** 2)
    return megabytes

def convert_bytes_to_gigabytes(bytes):
    gigabytes = bytes / (1024 ** 3)
    return gigabytes

def convert_bytes_to_terabytes(bytes):
    terabytes = bytes / (1024 ** 4)
    return terabytes

def main():
    bits = int(input("Enter the number of bits: "))

    bytes = convert_bits_to_bytes(bits)
    megabytes = convert_bytes_to_megabytes(bytes)
    gigabytes = convert_bytes_to_gigabytes(bytes)
    terabytes = convert_bytes_to_terabytes(bytes)

    print(f"{bits} bits is equal to:")
    print(f"{bytes:.4f} bytes")
    print(f"{megabytes:.4f} megabytes")
    print(f"{gigabytes:.4f} gigabytes")
    print(f"{terabytes:.4f} terabytes")

if __name__ == "__main__":
    main()
