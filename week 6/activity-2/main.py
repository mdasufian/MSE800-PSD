from authentication import login


# Entry-point class for the Zoo admin login demo.
class ZooApp:
    def run(self):
        print("=== Welcome to the Zoo Admin Login ===")
        username = input("Enter admin username: ")
        password = input("Enter password: ")

        # login() is wrapped by the validate_password decorator,
        # so the returned value comes from the decorator.
        result = login(username, password)
        print(f"Login result from decorator: {result}")


if __name__ == "__main__":
    app = ZooApp()
    app.run()
