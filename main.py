from wit import Wit
import os

if __name__ == "__main__":
    # test_data = {
    #     "greeting" : [
    #         "Hello",
    #         "Hi",
    #         "How are you?",
    #         "Good day"
    #         ],
    #     "farewell" : [
    #         "Bye",
    #         "Goodbye",
    #         "See you later"
    #     ]
    # }

    client = Wit(os.environ.get("ACCESS_TOKEN"))
    client.interactive()
