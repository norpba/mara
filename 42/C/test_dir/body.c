/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   body.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/04 08:28:51 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/04 12:40:10 by hniinima         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void ft_putchar (char c);

void ft_print_sign(int x, int y, int i, int j);

void ft_body(int x, int y)
{
	int i;
	int j;

	j = 0;
	while (j < y+1)
	{
		i = 0;
		while (i < x+1)
		{
			ft_print_sign(x, y, i, j);
			i++;
		} ft_putchar('\n');
		j++;
	}
}

void	ft_print_sign(int x_max, int y_max, int x_arvo, int y_arvo)
{
	/*if (j == 0 || j == y - 1)
	{
		if(i == 0)
			ft_putchar('/');
		else if (i == x - 1)
			ft_putchar('\\');
		else
			ft_putchar('*');
	}
	else
	{
		if (i == 0 || i == x - 1)
			ft_putchar('|');
		else
			ft_putchar(' ');
	}*/
	printf("x_arvo = %d   y_arvo = %d   x_max = %d   y_max = %d\n", x_arvo, y_arvo, x_max, y_max);
	
	if ((x_arvo == 1 && y_arvo == 1) || (x_arvo == x_max && y_arvo == y_max))
		ft_putchar('/');
	
	else if ((y_arvo == 1 && x_arvo == x_max) || (x_arvo == 1 && y_arvo == y_max))
		ft_putchar('\\');
	
	else if ((y_arvo == 1 || y_arvo == y_max) && (x_arvo > 1 && x_arvo < x_max))
		ft_putchar('*');
	
	else if ((y_arvo > 1 && y_arvo < y_max) && (x_arvo == 1 || x_arvo == x_max))
		ft_putchar('|');
	else
		ft_putchar(' ');	
}
