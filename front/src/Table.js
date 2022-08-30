import React, { useEffect, useState } from "react"
import StyledTable from "./styles"
import {
    createColumnHelper,
    flexRender,
    getCoreRowModel,
    useReactTable,
  } from '@tanstack/react-table'
  
const columnHelper = createColumnHelper()

const columns = [
  columnHelper.accessor('ticker', {
    header:  'ticker',
    cell: info => info?.getValue(),
  }),
  columnHelper.accessor('volume', {
    header:  'volume',
    cell: info => info?.getValue(),
  }),
  columnHelper.accessor('price', {
    header: 'price',
    cell: info => info?.getValue(),
  }),
  columnHelper.accessor('user_name', {
    header: 'user_name',
    cell: info => info?.getValue(),
  }),
  columnHelper.accessor('user_email', {
    header: 'user_email',
    cell: info => info?.getValue(),
  }),
]

const Table = ({ data }) => {

  const [dados, setDados] = React.useState(()=>[...data])

  useEffect(() =>{ 
    setDados(data)
  }, [data])


  const table = useReactTable({
    dados,
    columns,
    getCoreRowModel: getCoreRowModel(),
  })
 

  return (
    <StyledTable>
      <table>
        <thead>
          <tr>
            <th>ticker</th>
            <th>volume</th>
            <th>price</th>
            <th>user_name</th>
            <th>user_email</th>
          </tr>
        </thead>
        <tbody>
          {data.map((user, key) => (
            <tr key={key}>
              <td>{user.ticker}</td>
              <td>{user.volume}</td>
              <td>{user.price}</td>
              <td>{user.user_name}</td>
              <td>{user.user_email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </StyledTable>
  );
}

export default Table

