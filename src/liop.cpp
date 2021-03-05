#include <MyDescriptors.h>
#include "Utils.h"

extern "C" float* detect(int, int, void*, int , void*);
int* detect(int w,
			int h,
			void* img,
			int len, 
			void* kp,
			){
/*		
 * img is expected as unisgned char array
 */
	Params params;
	params.des_type = LIOP;
	params.initSigma= 1.0;
	params.srNum = 1;
	params.liopType = 1;
	params.liopRegionNum = 6;
	params.liopNum = 4;
	GeneratePatternMap(&params.pLiopPatternMap, &params.pLiopPosWeight, params.liopNum);

	params.lsRadius = 6;
	params.normPatchWidth = 41;
	params.nSigma =  1.2;
	params.liopThre = 5.0;

	Mat KP(cv::Size(len,5), cv::CV_32FC1, (float* kp));
	vector<AffineKeyPoint> kpts;
	for(int l=0; l<L; l++){
		kpts.push_back(AffineKeyPoint(KP[l,0],
									  KP[l,1],
								      KP[l,2],
								      KP[l,3],
								      KP[l,4]))
	}

	Mat dess;

	//read image and affine regions
	Mat img_byte(cv::Size(w,h), cv::CV_8UC1, (uchar*)img);
	Mat img;
	img_byte.convertTo(img, cv::CV_32FC1);

	if (params.initSigma > 0){
		GaussianBlur(img, img, Size(0, 0), params.initSigma);
	}

	//extract descriptors
	MyDescriptors commonDes(params);
	commonDes.compute(img, kpts, dess);
	return dess;	
//	WriteDess(des_file, kpts, dess, params.desFormat);
//	return 0;
}
