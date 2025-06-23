origin_image = open("dog.jpg", "rb")
receive_image = open("read_in.jpg", "rb")

iterations = 0
successes = 0

while True:
    origin_byte_data = origin_image.read(1)
    receive_byte_data = receive_image.read(1)

    if not origin_byte_data:
        break

    iterations += 1

    if origin_byte_data == receive_byte_data:
        successes += 1

print(iterations)
print("BER:", successes/iterations * 100, "%")