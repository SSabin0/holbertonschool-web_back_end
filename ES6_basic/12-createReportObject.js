function createEmployeesObject(departmentName, employees) {
  const departmentEmployee = {
    [`${departmentName}`]: employees,
  };
  return departmentEmployee;
}

function createReportObject(employeesList) {
  return {
    allEmployees: { ...employeesList },
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}
