## TEST PLAN

## 1. General

### Test 1.1 - File is linked appropriately

## 2. Print Menu Function

### Test 2.1 - Returns a string

### Test 2.2 - Returns menu in desired format

## 3. Print Category Function

### Test 3.1 - Returns a string

### Test 3.2 - Returns category section of menu in desired format

### Test 3.3 - Works with various widths

## 4. Greeting Function

### NOTE: This function only prints, doesn't return. How to test?

## 5. Check Input Function
This function is used to read and parse out (when necessary) what the user types into the command line. Many of the commands are simply passed on to the feedback function.

### Test 5.1 When input is 'order' returns 'order'

### Test 5.2 When input is 'menu' returns 'menu'

### Test 5.3.1 When input is remove <item>, item is decremented from a dict named ORDER and returns 'removed <item>'

### Test 5.3.2 If the item typed into 'remove <item>' is not in the ORDER, returns 'That item is not in your order!'

### Test 5.4 If the user types something that is not a valid command, returns 'N/A'

## 6. Feedback function
This function takes the output from the check input function and prints feedback to the user

### 6.1 Returns a string

### 6.2 If the input is 'N/A' or an empty string, returns 'Sorry, I didn't understand. :('

