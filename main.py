import sys

from data.geocoder import get_ll_span
from data.mapapi_PG import show_map

toponym_to_find = " ".join(sys.argv[1:])

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    ll_spn = f"ll={ll}&spn={spn}"
    # добавим точку, чтобы указать найденный объект
    point_param = f"pt={ll}"

    show_map(ll_spn, "map", add_params=point_param)
