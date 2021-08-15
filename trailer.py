import fresh_tomatoes
import movie_tralier_class





sahoo=movie_tralier_class.Movie("sahoo",
                                "how did king got his kingdom back",
                                "https://upload.wikimedia.org/wikipedia/en/6/6b/Saaho_poster.jpg",
                                "https://www.youtube.com/watch?v=HNnt00swZ5Q&ab_channel=UVCreations")




ms_dhoni=movie_tralier_class.Movie("ms_dhoni",
                                   "the untold story of mahi",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg/220px-M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                                   "https://www.youtube.com/watch?v=SiZbhos1LPA&ab_channel=FoxStarHindi")


pushpa=movie_tralier_class.Movie("pushpa",
                                 "the pushpa",
                                 "https://th.bing.com/th/id/OIP.5WOaY-M-Xwd2p_qrBC_Q3AHaK1?w=115&h=180&c=7&o=5&pid=1.7",
                                 "https://www.youtube.com/watch?v=Lk2oDvoonUc&ab_channel=MythriMovieMakers")

movies=[sahoo, ms_dhoni, pushpa]
fresh_tomatoes.open_movies_page(movies)

print("end")
                            
