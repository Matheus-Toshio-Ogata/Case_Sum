# Task 2

## Django
- Your next goal is to implement a filter for trading blotters instances
- The filter should work for any blotter attribute. The attribute that should be filtered must be in the request.
- Don't forget to check the recommended tools and libraries, specially the [Filtering section](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend).

## React
- You should implement a text field filter getting the user input and sending to the API a request to filter by `ticker` attribute.
- You may use Material UI components or a basic HTML input field.
- This field must be [debounced](https://lodash.com/docs/4.17.15#debounce), in other words, it should only send the request after the user stops typing, usually after 500ms.

### VALE3
ticker | volume | price | user_name | user_email
--- | --- | --- | --- | ---
VALE3 | 100 | 27.50 | John | John@bank1
VALE3 | 100 | 27.60 | John | John@bank1
VALE3 | 200 | 26.30 | John | John@bank1
VALE3 | 300 | 26.00 | John | John@bank1

### ABCD11 (no blotters found)
ticker | volume | price | user_name | user_email
--- | --- | --- | --- | ---
