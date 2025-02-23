def isPalindrome(self, s: str) -> bool:

    if not s:
        return True

    cleaned_str = ''.join(ch for ch in s if ch.isalnum())
    result_string = cleaned_str.lower()

    # result_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # 2nd Solution 

    if result_string == result_string[::-1]:
        return True
  
    return False
