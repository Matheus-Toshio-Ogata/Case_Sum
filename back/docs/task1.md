# Task 1
_Don't forget to setup your environment._

## Django (Backend)

- You will have two models: Blotter and User. Each blotter instance has some trading information and a user.
- The default output for `http://localhost:8000/trading/blotter/` is:

```json
[
    {
        "id": 1,
        "ticker": "PETR4",
        "volume": 100,
        "price": 27,
        "user": 1
    },
    {
        "id": 2,
        "ticker": "VALE3",
        "volume": 150000,
        "price": 79,
        "user": 1
    },
    {
        "id": 3,
        "ticker": "BOVA11",
        "volume": 2022,
        "price": 97,
        "user": 1
    },
    ...
```

- Your first goal is to return the name and the email of the user for each blotter, for example:

```json
[
    {
        "id": 1,
        "ticker": "PETR4",
        "volume": 100,
        "price": 27,
        "user": 1,
        "user_name": "John",
        "user_email": "John@bank1"
    },
    {
        "id": 2,
        "ticker": "VALE3",
        "volume": 150000,
        "price": 79,
        "user": 1,
        "user_name": "John",
        "user_email": "John@bank1"
    },
    {
        "id": 3,
        "ticker": "BOVA11",
        "volume": 2022,
        "price": 97,
        "user": 1,
        "user_name": "John",
        "user_email": "John@bank1"
    },
    ....
]
```

## React (Frontend)

- Fetch data from `http://localhost:8000/trading/blotter/` every minute.
- Create a table component (Table.js).
- App.js gets fetched data and pass it as a prop to the Table.js component:
```js
<Table data={
	[
		{
        "id": 1,
        "ticker": "PETR4",
        "volume": 100,
        "price": 27,
        "user": 1,
        "user_name": "John",
        "user_email": "John@bank1"
	    },
	    ...
	]
}/>
```

Example:

ticker | volume | price | user_name | user_email
--- | --- | --- | --- | ---
PETR4 | 100 | 27.5 | John | John@bank1


Styles should be done on a external file named `styles.js`  [Styled-component](https://styled-components.com/) (already installed and ready to use)

