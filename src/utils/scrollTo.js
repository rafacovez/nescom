export function scrollTo(selector) {
  const element = document.querySelector(selector);
  element.scrollIntoView({ behavior: "smooth" });
}
