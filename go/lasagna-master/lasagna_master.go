package lasagna

func PreparationTime(layers []string, average int) int {
	if average == 0 {
		average = 2
	}
	return len(layers) * average
}

func Quantities(layers []string) (noodles int, sauce float64) {
	for _, v := range layers {
		switch v {
		case "noodles":
			noodles += 50
		case "sauce":
			sauce += 0.2
		}
	}
	return
}

func AddSecretIngredient(friends, mine []string) {
	ingredient := friends[len(friends)-1]
	mine[len(mine)-1] = ingredient
}

func ScaleRecipe(quantities []float64, portions int) []float64 {
	scale := float64(portions) / 2.0
	amounts := make([]float64, 0, len(quantities))
	for _, v := range quantities {
		amounts = append(amounts, v*scale)
	}
	return amounts
}
