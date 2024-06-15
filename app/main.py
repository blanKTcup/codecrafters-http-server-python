import socket


def main():
    # Creates a TCP/IP socket
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
      # Wait for a connection
      print("Waiting for a connection...")
      connection, address = server_socket.accept() # wait for client
      
      print(f"Accepted connection from {address}")

      # Sends a 200 OK response
      response = "HTTP/1.1 200 OK\r\n\r\n"
      connection.sendall(response.encode())


if __name__ == "__main__":
    main()
