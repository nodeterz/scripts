#!/bin/sh
#SBATCH --job-name="vasp"
#SBATCH --exclusive=user
#SBATCH --ntasks=16
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=1
#SBATCH --qos=kernph-1week
#SBATCH --partition=psi
#SBATCH --mem-per-cpu=1700M

cp -r ../../template_Au/ 00151 && cd 00151  && cp ../data/tt00151 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00152 && cd 00152  && cp ../data/tt00152 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00153 && cd 00153  && cp ../data/tt00153 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00154 && cd 00154  && cp ../data/tt00154 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00155 && cd 00155  && cp ../data/tt00155 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00156 && cd 00156  && cp ../data/tt00156 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00157 && cd 00157  && cp ../data/tt00157 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00158 && cd 00158  && cp ../data/tt00158 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00159 && cd 00159  && cp ../data/tt00159 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00160 && cd 00160  && cp ../data/tt00160 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00161 && cd 00161  && cp ../data/tt00161 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00162 && cd 00162  && cp ../data/tt00162 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00163 && cd 00163  && cp ../data/tt00163 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00164 && cd 00164  && cp ../data/tt00164 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00165 && cd 00165  && cp ../data/tt00165 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00166 && cd 00166  && cp ../data/tt00166 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00167 && cd 00167  && cp ../data/tt00167 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00168 && cd 00168  && cp ../data/tt00168 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00169 && cd 00169  && cp ../data/tt00169 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00170 && cd 00170  && cp ../data/tt00170 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00171 && cd 00171  && cp ../data/tt00171 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00172 && cd 00172  && cp ../data/tt00172 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00173 && cd 00173  && cp ../data/tt00173 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00174 && cd 00174  && cp ../data/tt00174 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00175 && cd 00175  && cp ../data/tt00175 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00176 && cd 00176  && cp ../data/tt00176 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00177 && cd 00177  && cp ../data/tt00177 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00178 && cd 00178  && cp ../data/tt00178 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00179 && cd 00179  && cp ../data/tt00179 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00180 && cd 00180  && cp ../data/tt00180 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00181 && cd 00181  && cp ../data/tt00181 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00182 && cd 00182  && cp ../data/tt00182 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00183 && cd 00183  && cp ../data/tt00183 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00184 && cd 00184  && cp ../data/tt00184 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00185 && cd 00185  && cp ../data/tt00185 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00186 && cd 00186  && cp ../data/tt00186 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00187 && cd 00187  && cp ../data/tt00187 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00188 && cd 00188  && cp ../data/tt00188 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00189 && cd 00189  && cp ../data/tt00189 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00190 && cd 00190  && cp ../data/tt00190 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00191 && cd 00191  && cp ../data/tt00191 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00192 && cd 00192  && cp ../data/tt00192 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00193 && cd 00193  && cp ../data/tt00193 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00194 && cd 00194  && cp ../data/tt00194 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00195 && cd 00195  && cp ../data/tt00195 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00196 && cd 00196  && cp ../data/tt00196 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00197 && cd 00197  && cp ../data/tt00197 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00198 && cd 00198  && cp ../data/tt00198 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00199 && cd 00199  && cp ../data/tt00199 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00200 && cd 00200  && cp ../data/tt00200 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00201 && cd 00201  && cp ../data/tt00201 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00202 && cd 00202  && cp ../data/tt00202 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00203 && cd 00203  && cp ../data/tt00203 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00204 && cd 00204  && cp ../data/tt00204 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00205 && cd 00205  && cp ../data/tt00205 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00206 && cd 00206  && cp ../data/tt00206 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00207 && cd 00207  && cp ../data/tt00207 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00208 && cd 00208  && cp ../data/tt00208 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00209 && cd 00209  && cp ../data/tt00209 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00210 && cd 00210  && cp ../data/tt00210 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00211 && cd 00211  && cp ../data/tt00211 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00212 && cd 00212  && cp ../data/tt00212 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00213 && cd 00213  && cp ../data/tt00213 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00214 && cd 00214  && cp ../data/tt00214 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00215 && cd 00215  && cp ../data/tt00215 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00216 && cd 00216  && cp ../data/tt00216 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00217 && cd 00217  && cp ../data/tt00217 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00218 && cd 00218  && cp ../data/tt00218 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00219 && cd 00219  && cp ../data/tt00219 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00220 && cd 00220  && cp ../data/tt00220 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00221 && cd 00221  && cp ../data/tt00221 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00222 && cd 00222  && cp ../data/tt00222 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00223 && cd 00223  && cp ../data/tt00223 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00224 && cd 00224  && cp ../data/tt00224 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00225 && cd 00225  && cp ../data/tt00225 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00226 && cd 00226  && cp ../data/tt00226 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00227 && cd 00227  && cp ../data/tt00227 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00228 && cd 00228  && cp ../data/tt00228 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00229 && cd 00229  && cp ../data/tt00229 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00230 && cd 00230  && cp ../data/tt00230 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00231 && cd 00231  && cp ../data/tt00231 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00232 && cd 00232  && cp ../data/tt00232 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00233 && cd 00233  && cp ../data/tt00233 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00234 && cd 00234  && cp ../data/tt00234 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00235 && cd 00235  && cp ../data/tt00235 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00236 && cd 00236  && cp ../data/tt00236 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00237 && cd 00237  && cp ../data/tt00237 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00238 && cd 00238  && cp ../data/tt00238 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00239 && cd 00239  && cp ../data/tt00239 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00240 && cd 00240  && cp ../data/tt00240 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00241 && cd 00241  && cp ../data/tt00241 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00242 && cd 00242  && cp ../data/tt00242 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00243 && cd 00243  && cp ../data/tt00243 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00244 && cd 00244  && cp ../data/tt00244 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00245 && cd 00245  && cp ../data/tt00245 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00246 && cd 00246  && cp ../data/tt00246 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00247 && cd 00247  && cp ../data/tt00247 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00248 && cd 00248  && cp ../data/tt00248 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00249 && cd 00249  && cp ../data/tt00249 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00250 && cd 00250  && cp ../data/tt00250 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00251 && cd 00251  && cp ../data/tt00251 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00252 && cd 00252  && cp ../data/tt00252 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00253 && cd 00253  && cp ../data/tt00253 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00254 && cd 00254  && cp ../data/tt00254 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00255 && cd 00255  && cp ../data/tt00255 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00256 && cd 00256  && cp ../data/tt00256 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00257 && cd 00257  && cp ../data/tt00257 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00258 && cd 00258  && cp ../data/tt00258 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00259 && cd 00259  && cp ../data/tt00259 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00260 && cd 00260  && cp ../data/tt00260 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00261 && cd 00261  && cp ../data/tt00261 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00262 && cd 00262  && cp ../data/tt00262 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00263 && cd 00263  && cp ../data/tt00263 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00264 && cd 00264  && cp ../data/tt00264 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00265 && cd 00265  && cp ../data/tt00265 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00266 && cd 00266  && cp ../data/tt00266 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00267 && cd 00267  && cp ../data/tt00267 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00268 && cd 00268  && cp ../data/tt00268 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00269 && cd 00269  && cp ../data/tt00269 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00270 && cd 00270  && cp ../data/tt00270 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00271 && cd 00271  && cp ../data/tt00271 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00272 && cd 00272  && cp ../data/tt00272 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00273 && cd 00273  && cp ../data/tt00273 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00274 && cd 00274  && cp ../data/tt00274 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00275 && cd 00275  && cp ../data/tt00275 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00276 && cd 00276  && cp ../data/tt00276 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00277 && cd 00277  && cp ../data/tt00277 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00278 && cd 00278  && cp ../data/tt00278 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00279 && cd 00279  && cp ../data/tt00279 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00280 && cd 00280  && cp ../data/tt00280 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00281 && cd 00281  && cp ../data/tt00281 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00282 && cd 00282  && cp ../data/tt00282 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00283 && cd 00283  && cp ../data/tt00283 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00284 && cd 00284  && cp ../data/tt00284 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00285 && cd 00285  && cp ../data/tt00285 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00286 && cd 00286  && cp ../data/tt00286 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00287 && cd 00287  && cp ../data/tt00287 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00288 && cd 00288  && cp ../data/tt00288 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00289 && cd 00289  && cp ../data/tt00289 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00290 && cd 00290  && cp ../data/tt00290 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00291 && cd 00291  && cp ../data/tt00291 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00292 && cd 00292  && cp ../data/tt00292 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00293 && cd 00293  && cp ../data/tt00293 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00294 && cd 00294  && cp ../data/tt00294 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00295 && cd 00295  && cp ../data/tt00295 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00296 && cd 00296  && cp ../data/tt00296 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00297 && cd 00297  && cp ../data/tt00297 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00298 && cd 00298  && cp ../data/tt00298 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00299 && cd 00299  && cp ../data/tt00299 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..
cp -r ../../template_Au/ 00300 && cd 00300  && cp ../data/tt00300 POSCAR && mpirun -n 16 ~/bin/vasp_std >o1 && cd ..