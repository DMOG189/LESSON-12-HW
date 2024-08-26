# HOMEWORK 1 SET



# SET
# 1. Add Emma Watson to the Oscar winners set.
# 2. Clear the Oscar winners set.
# 3. Create a copy of the Oscar winners set.
# 4. Remove Meryl Streep from the Oscar winners set.
# 5. Which actors appeared in both Titanic and The Dark Knight?
# 6. Are there any actors who appeared in both Iron Man and Avengers?
# 7. Did all actors in actor_list win an Oscar?
# 8. Does actor_list include all actors who appeared in Avengers?
# 9. Remove one actor at random from movie_cast.
# 10. Remove Matt Damon from movie_cast.
# 11. Which actors in Titanic did not win an Oscar?
# 12. Which actors appeared in only one of the movies, Titanic or The Dark Knight?
# 13. Update the Oscar winners set to include Cate Blanchett and Daniel Day-Lewis.
# 14. Unite the Titanic and The Dark Knight actors to see all the actors’ names.
# 15. Check if all actors in dark_knight_actors also appeared in The Dark Knight Rises.
# 16. Check if legendary_actors includes all Oscar winners.
# 17. Which actors in Avengers did not appear in Iron Man?
# 18. Which actors appeared in only one of the movies, The Dark Knight or Avengers?
# 19. Unite The Dark Knight and Iron Man actors to see all the actors’ names.
# 20. Create a frozen set from legendary_actors.




# START

# GIVEN SET:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}

dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}

avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
                   "Chris Hemsworth", "Jeremy Renner"}

iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}

legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}

actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}

movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# 1. Add Emma Watson to the Oscar winners set:
oscar_winners.add("Emma Watson")
print(oscar_winners)

# 2. Clear the Oscar winners set:
oscar_winners.clear()
print(oscar_winners)

# 3. Create a copy of the Oscar winners set:
oscar_winners_copy = oscar_winners.copy()
print(oscar_winners_copy)

# 4. Remove Meryl Streep from the Oscar winners set:
oscar_winners.discard("Meryl Streep")
print(oscar_winners)

# 5. Which actors appeared in both Titanic and The Dark Knight?
common_actors = titanic_actors.intersection(dark_knight_actors)
print(common_actors)

# 6. Are there any actors who appeared in both Iron Man and Avengers?
common_actors = iron_man_actors.intersection(avengers_actors)
print(common_actors)

# 7. Did all actors in actor_list win an Oscar?
all_won_oscar = actor_list.issubset(oscar_winners)
print(all_won_oscar)

# 8. Does actor_list include all actors who appeared in Avengers?
contains_all_avengers = avengers_actors.issubset(actor_list)
print(contains_all_avengers)

# 9. Remove one actor at random from movie_cast:
removed_actor = movie_cast.pop()
print(f"Removed: {removed_actor}")
print(movie_cast)

# 10. Remove Matt Damon from movie_cast:
movie_cast.discard("Matt Damon")
print(movie_cast)

# 11. Which actors in Titanic did not win an Oscar?
non_oscar_winners = titanic_actors.difference(oscar_winners)
print(non_oscar_winners)

# 12. Which actors appeared in only one of the movies, Titanic or The Dark Knight?
exclusive_actors = titanic_actors.symmetric_difference(dark_knight_actors)
print(exclusive_actors)

# 13. Update the Oscar winners set to include Cate Blanchett and Daniel Day-Lewis:
oscar_winners.update(["Cate Blanchett", "Daniel Day-Lewis"])
print(oscar_winners)

# 14. Unite the Titanic and The Dark Knight actors to see all the actors’ names:
all_actors = titanic_actors.union(dark_knight_actors)
print(all_actors)

# 15. Check if all actors in dark_knight_actors also appeared in The Dark Knight Rises:
dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman", "Tom Hardy", "Joseph Gordon-Levitt"}
all_in_rises = dark_knight_actors.issubset(dark_knight_rises_actors)
print(all_in_rises)

# 16. Check if legendary_actors includes all Oscar winners:
legendary_contains_all_oscar = oscar_winners.issubset(legendary_actors)
print(legendary_contains_all_oscar)

# 17. Which actors in Avengers did not appear in Iron Man?
non_iron_man_actors = avengers_actors.difference(iron_man_actors)
print(non_iron_man_actors)

# 18. Which actors appeared in only one of the movies, The Dark Knight or Avengers?
exclusive_to_one_movie = dark_knight_actors.symmetric_difference(avengers_actors)
print(exclusive_to_one_movie)

# 19. Unite The Dark Knight and Iron Man actors to see all the actors’ names:
all_superhero_actors = dark_knight_actors.union(iron_man_actors)
print(all_superhero_actors)

# 20. Create a frozen set from legendary_actors:
frozen_legendary_actors = frozenset(legendary_actors)
print(frozen_legendary_actors)


# END


