# import os
# import socket

# address = '/tmp/socket'
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(address)      # this creates the socket file
# s.listen(1)
# r, a = s.accept()
# r.send('Hello\n')
# msg = r.recv(1024)
# print (msg)
# r.close()
# s.close()
# os.unlink(address)    # remove the socket file so that it can be recreated on next run
def calculate_checksum(data):
    # Tính toán checksum bằng cách cộng tất cả các byte trong dữ liệu
    checksum = sum(data)

    # Trả về giá trị checksum, thường được biểu diễn dưới dạng một số nguyên 8-bit
    return checksum & 0xFF

def add_checksum(data):
    # Tính toán checksum của dữ liệu
    checksum = calculate_checksum(data)

    # Thêm checksum vào cuối dữ liệu
    data_with_checksum = data + [checksum]

    return data_with_checksum

def verify_checksum(data_with_checksum):
    # Tách checksum từ cuối dữ liệu
    received_checksum = data_with_checksum[-1]

    # Loại bỏ checksum từ dữ liệu
    data_without_checksum = data_with_checksum[:-1]

    # Tính toán checksum của dữ liệu
    calculated_checksum = calculate_checksum(data_without_checksum)

    # So sánh checksum nhận được với checksum tính toán
    return received_checksum == calculated_checksum

# Ví dụ sử dụng
original_data = [0x01, 0x02, 0x03, 0x04]

# Thêm checksum vào dữ liệu
data_with_checksum = add_checksum(original_data)

# Kiểm tra tính toàn vẹn của dữ liệu với checksum
is_valid = verify_checksum(data_with_checksum)

print(f"Original Data: {original_data}")
print(f"Data with Checksum: {data_with_checksum}")
print(f"Checksum is Valid: {is_valid}")
