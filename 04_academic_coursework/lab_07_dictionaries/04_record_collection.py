"""
Lab 7 - Exercise 4: Record Collection Manager
=============================================
Manages a musical record collection database using nested dictionary operations.
Allows updating album properties, managing track lists, and deleting attributes.
"""

from typing import Any, Dict, List, Union


def update_records(
    records: Dict[int, Dict[str, Any]],
    record_id: int,
    prop: str,
    value: Union[str, List[str]],
) -> Dict[int, Dict[str, Any]]:
    """Update album record with property mutation rules.

    Rules:
    - If value is empty string, delete the property.
    - If prop is not 'tracks' and value is non-empty, assign value.
    - If prop is 'tracks': create list if not present, and append item(s).
    """
    if record_id not in records:
        records[record_id] = {}

    album = records[record_id]

    if value == "":
        album.pop(prop, None)
    elif prop != "tracks":
        album[prop] = value
    else:
        if "tracks" not in album:
            album["tracks"] = []

        if isinstance(value, list):
            album["tracks"].extend(value)
        else:
            album["tracks"].append(value)

    return records


if __name__ == "__main__":
    record_collection = {
        2548: {
            "albumTitle": "Slippery When Wet",
            "artist": "Bon Jovi",
            "tracks": ["Let It Rock", "You Give Love a Bad Name"],
        },
        2468: {
            "albumTitle": "1999",
            "artist": "Prince",
            "tracks": ["1999", "Little Red Corvette"],
        },
        1245: {
            "artist": "Robert Palmer",
            "tracks": [],
        },
        5439: {
            "albumTitle": "ABBA Gold",
        },
    }

    # Test artist update
    update_records(record_collection, 2548, "artist", "Sting")
    assert record_collection[2548]["artist"] == "Sting"

    # Test property deletion
    update_records(record_collection, 2548, "artist", "")
    assert "artist" not in record_collection[2548]

    # Test tracks appending
    update_records(record_collection, 5439, "tracks", "Take a Chance on Me")
    assert record_collection[5439]["tracks"] == ["Take a Chance on Me"]

    # Test multiple tracks appending via list
    update_records(record_collection, 1245, "tracks", ["Addicted to Love", "Simply Irresistible"])
    assert "Addicted to Love" in record_collection[1245]["tracks"]

    print("Record Collection Manager: All tests passed!")
