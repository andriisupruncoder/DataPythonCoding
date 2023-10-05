To create a table with 10 rows and 3 columns in React, where each table box is an input field, you can use the following functional component:

```javascript
import React, { useState } from 'react';

const TableComponent = () => {
  const initialData = Array(10).fill(Array(3).fill(''));

  const [tableData, setTableData] = useState(initialData);

  const handleInputChange = (rowIndex, colIndex, event) => {
    const updatedData = [...tableData];
    updatedData[rowIndex][colIndex] = event.target.value;
    setTableData(updatedData);
  };

  return (
    <table>
      <tbody>
        {tableData.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {row.map((cell, colIndex) => (
              <td key={colIndex}>
                <input
                  type="text"
                  value={cell}
                  onChange={(event) =>
                    handleInputChange(rowIndex, colIndex, event)
                  }
                />
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TableComponent;
```

In this component, `useState` maintains the state of the table's data. The `initialData` creates a 10x3 matrix filled with empty strings, which represents the table. The `handleInputChange` function updates the table state when a user inputs data. The `table` element contains rows rendered from the state, and each cell within a row is an input box that reflects and updates the component's state.

To use this component in your React app, you can simply import and render it as `<TableComponent />`.
