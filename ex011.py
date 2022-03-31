lgr = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
are = lgr * alt
print('sua parede tem a dimensao de {}X{} e sua area e de {}m²'.format(lgr, alt,are))
tinta = are / 2
print('para pinta essa parede, voce {}l de tinta.'.format(tinta))