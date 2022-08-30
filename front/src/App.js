import React, { useEffect, useState, useCallback } from "react"
import Table from "./Table"
import debounce from 'lodash.debounce';

const App = () => {
  const [users, setUsers] = useState([])
  const [inputData, setInputData] = useState("");
  const [dbInputData, setDbInputData] = useState('');
  const handleInputChange = (e) => {
	debouncedSave(e.target.value)
	setInputData(e.target.value);
  }
  const debouncedSave = useCallback(
	debounce(nextValue => setDbInputData(nextValue), 500),
	[], 
  );

  const fetchData = async () => {
	await fetch("http://localhost:8000/trading/blotter/?ticker=" + dbInputData, 
	{
		method: "get",
	})
	  .then(response => response.json())
	  .then(data => {
		setUsers(data)
	})
	}

	useEffect(() => {
		fetchData()
		const intervalo = setInterval(()=>fetchData(), 60000);
		return () => clearInterval(intervalo)
	  }, [dbInputData])
	
  return (
	<div className = "App">
		<input 
				onChange={handleInputChange}
				value={inputData}
				type="text"
				/>
		<Table data={users}/> 
		
	</div>
  );
}

export default App