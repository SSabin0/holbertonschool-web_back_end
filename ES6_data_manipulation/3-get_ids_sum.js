export default function getStudentIdsSum(list) {
  const sum = list.reduce((accumulator, current) => accumulator + current.id, 0);
  return sum;
}
