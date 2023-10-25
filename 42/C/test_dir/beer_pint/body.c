/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   body.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hniinima <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/04 12:27:38 by hniinima          #+#    #+#             */
/*   Updated: 2022/07/04 12:57:13 by hniinima         ###   ########.fr       */
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

void    ft_print_sign(int x_max, int y_max, int x_arvo, int y_arvo)
{
	//printf("x_arvo = %d   y_arvo = %d   x_max = %d   y_max = %d\n", x_arvo, y_arvo, x_max, y_max);

    if ((x_arvo == 1 && y_arvo == y_max) || (x_arvo == 4 && y_arvo == y_max))
        ft_putchar('|');

    else if ((y_arvo == y_max && x_arvo ==????? ) || (x_arvo == 1 && y_arvo == y_max))
        ft_putchar('_');
    else
        ft_putchar(' '); 
} 
