def tally(rows):
    db = {}

    for row in rows:
        team_one, team_two, match_result = row.split(";")

        team_one_entry = db.get(team_one, [team_one, 0, 0, 0, 0, 0])
        team_two_entry = db.get(team_two, [team_two, 0, 0, 0, 0, 0])

        team_one_entry[1] += 1
        team_two_entry[1] += 1

        if match_result == "win":
            team_one_entry[2] += 1
            team_one_entry[5] += 3
            team_two_entry[4] += 1
        elif match_result == "draw":
            team_one_entry[3] += 1
            team_one_entry[5] += 1
            team_two_entry[3] += 1
            team_two_entry[5] += 1
        elif match_result == "loss":
            team_one_entry[4] += 1
            team_two_entry[2] += 1
            team_two_entry[5] += 3

        db[team_one] = team_one_entry
        db[team_two] = team_two_entry

    results = sorted(list(db.values()), key=lambda i: (-i[-1], i[0]))

    table = ["Team                           | MP |  W |  D |  L |  P"]

    for team, mp, w, d, l, p in results:
        line = f"{team:<30} | {mp:>2} | {w:>2} | {d:>2} | {l:>2} | {p:>2}"
        table.append(line)

    return table
