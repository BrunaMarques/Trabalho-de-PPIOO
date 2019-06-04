from trabalho import *

#função lexer
assert lexer("2+3") == [2, "+", 3]
assert lexer("4 + 3 + 5") == [4, "+", 3, "+", 5]
assert lexer("((18 + 3 * 2) / 8 + 5 * 3) / 6") == ["(", "(", 18, "+", 3, "*", 2, ")", "/", 8, "+", 5, "*", 3, ")", "/", 6]
assert lexer("(((8 * 4 + 3) / 7 + (3 + 15 / 5) * 3) * 2 -(19 - 7) / 6) * 2 + 12") == ["(", "(", "(", 8, "*", 4, "+", 3, ")", "/", 7, "+", "(", 3, "+", 15, "/", 5, ")", "*", 3, ")", "*", 2, "-", "(", 19, "-", 7, ")", "/", 6, ")", "*", 2, "+", 12]
assert lexer("-20 + -51 + 20 + -68 * -11 + -35 * -14 - 95 - 32 + -52 * -23 - -90 * -42") == [-20, "+", -51, "+", 20, "+", -68, "*", -11, "+", -35, "*", -14, "-", 95, "-", 32, "+", -52, "*", -23, "-", -90, "*", -42]
assert lexer("(2 - 65 - (-24 + -97) * -5 * -61) * (-41 + 85 * 9 * -92 * (75 - 18))") == ["(", 2, "-", 65, "-", "(", -24, "+", -97, ")", "*", -5, "*", -61, ")", "*", "(", -41, "+", 85, "*", 9, "*", -92, "*", "(", 75, "-", 18, ")", ")"]
assert lexer("55 * 48 * -44 - -32 + 1 * -80 * -94 - 74 * -53 + -30 + -61") == [55, "*", 48, "*", -44, "-", -32, "+", 1, "*", -80, "*", -94, "-", 74, "*", -53, "+", -30, "+", -61]

#função Parser
assert Parser([2, 3, "+"]) == [Tree("+", 2, 3)]
assert Parser([2, 3 , "+", 4, "+"]) == [Tree("+", 4, Tree("+", 2, 3))]
assert Parser([18, 3, 2, '*', '+', 8, '/', 5, 3, '*', '+', 6, '/']) == [Tree("/",Tree("+", Tree("/", Tree("+", 18, Tree("*", 3, 2)),8), Tree("*", 5, 3)),6)]    


#função evalStep
assert evalStep(Tree("+", 2, 3)) == 5
assert evalStep(Tree("+", 4, Tree("+", 2, 3))) == Tree("+", 4, 5)
assert evalStep(Tree("/",Tree("+", Tree("/", Tree("+", 18, Tree("*", 3, 2)),8), Tree("*", 5, 3)),6)) == (Tree("/",Tree("+", Tree("/", Tree("+", 18, 6),8), Tree("*", 5, 3)),6))
assert evalStep(Tree("/",Tree("+", Tree("/", Tree("+", 18, 6),8), Tree("*", 5, 3)),6)) == Tree("/",Tree("+", Tree("/", 24 ,8), Tree("*", 5, 3)),6)
assert evalStep(Tree("/",Tree("+", Tree("/", 24 ,8), Tree("*", 5, 3)),6)) == Tree("/",Tree("+", 3 , Tree("*", 5, 3)),6)

#função toString
assert toString(Tree("+", 4, 5), "" ,0) == "4 + 5"
assert toString(Tree("/",Tree("+", Tree("/", Tree("+", 18, 6),8), Tree("*", 5, 3)),6), "", 0) == "((18 + 6) / 8 + 5 * 3) / 6" 
assert toString(Tree("/",Tree("+", Tree("/", 24 ,8), Tree("*", 5, 3)),6), "", 0) == "(24 / 8 + 5 * 3) / 6" 
assert toString(Tree("/",Tree("+", 3 , Tree("*", 5, 3)),6), "", 0) == "(3 + 5 * 3) / 6" 