const background = document.getElementById("LoginHero")
const loadinghero = document.getElementById("")











function confirm_delete_destination(destination_pk) {
    const ok = confirm("Delete this destination?")
    if (!ok) return

    mix_fetch(`/destinations/${destination_pk}`, "DELETE", null, true, false, false)
}