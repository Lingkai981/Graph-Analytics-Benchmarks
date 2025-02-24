#include "../core/flash2.h"

int main(int argc, char *argv[]) {
	VertexType(float,dis);
	SetDataset(argv[1], argv[2]);
	int s = atoi(argv[3]);

	VSet A=All.Local(v.dis=(v_id==s?0:-1)).Filter(v_id==s);

	for(int len = A.size(), i = 0; len > 0; len = A.size(), ++i) {
		print("Round %d: size=%d\n", i, len);
		if(len > n_vertex/50) A = All.Pull(for_nb(if(nb.dis>-0.5 && (v.dis<0 || nb.dis+1<v.dis)) v.dis=nb.dis+1));
		else A = A.Push(for_nb(
					if(nb.dis<0 || v.dis+1<nb.dis)
						push_to(nb_id, _v.dis=-1, if(_v.dis<0 || v.dis+1<_v.dis) _v.dis=v.dis+1)
				), if(dst.dis<0 || _v.dis<dst.dis) dst.dis=_v.dis);
	}

	print( "total time=%0.3lf secs\n", GetTime());
	//All.Gather(printf("id=%d,dis=%0.1f\n", v_id, v.dis));

	float td = 0;
	All.Local(if(v.dis>1e-8) td += v.dis); td = Sum(td);
	print("sum_dis=%0.3f\n", td);
	return 0;
	
}
