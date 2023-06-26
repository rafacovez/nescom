export function toggleNav(component) {
  if (component.screenWidth < 768) {
    component.navOpen = !component.navOpen;
    if (component.navOpen) {
      document.body.classList.add("no-scroll");
    } else {
      document.body.classList.remove("no-scroll");
    }
  }
}
