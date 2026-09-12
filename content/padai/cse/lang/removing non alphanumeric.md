**Using `str.isalnum()`**
text = "Hello, World! 123"
clean_text = ''.join(char for char in text if char.isalnum())
print(clean_text)  # Output: HelloWorld123   

 **Using Regular Expressions (`re.sub`)**
import re
text = "Hello, World! 123"
clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)
print(clean_text)  # Output: HelloWorld123   

**Preserving Spaces**
import re
text = "Hello, World! 123"
clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
print(clean_text)  # Output: Hello World 123   