export default function getStudentsByLocation(list, city) {
  const citylist = list.filter(n => n.location === city)
  return citylist;
}
