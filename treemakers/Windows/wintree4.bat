@ECHO off
color a
echo A COLOSSAL DIRECTORY
FOR %%A in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) DO (
	md %%A
	cd %%A
	FOR %%B in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) DO (
		md %%B
		cd %%B
		FOR %%C in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) DO (
			md %%C
			cd %%C
			FOR %%D in (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) DO (
				md %%D
			)
			cd ..
		)
		cd ..
	)
	cd ..
	echo 'finished %%A'
)
pause