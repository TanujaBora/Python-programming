def calculate_love_score(name1, name2):
    name = (name1 + name2).lower()
    print(name)
    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")
    true_count = t + r + u + e
    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e = name.count("e")
    love_count = l + o + v + e
    love_score = int(str(true_count)) + int(str(love_count))
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")


