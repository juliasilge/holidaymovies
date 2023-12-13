test_that("it is actually a wonderful life", {
  expect_equal(nchar(movie_wonderful_life()), 49)
})

test_that("a small child can defend their house", {
})

test_that("terrorists can be defeated at Christmastime", {
    expect_equal(toupper(movie_die_hard()), "YIPPEE-KI-YAY!")
})
