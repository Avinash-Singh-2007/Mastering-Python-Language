text = input("Enter comment: ")
if "make a lot of money" in text.lower() or "buy now" in text.lower() or "subscribe this" in text.lower() or "click this" in text.lower():
    print("Spam")
else:
    print("Not Spam")
