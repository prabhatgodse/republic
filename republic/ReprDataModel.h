//
//  ReprDataModel.h
//  republic
//
//  Created by Prabhat Godse on 1/2/17.
//  Copyright © 2017 Prabhat Godse. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <UIKit/UIKit.h>
#import <IGListKit/IGListKit.h>

@interface ReprDataModel : NSObject <IGListDiffable>

@property (nonatomic, copy) NSString *twitter;
@end
