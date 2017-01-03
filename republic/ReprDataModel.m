//
//  ReprDataModel.m
//  republic
//
//  Created by Prabhat Godse on 1/2/17.
//  Copyright © 2017 Prabhat Godse. All rights reserved.
//

#import "ReprDataModel.h"

@implementation ReprDataModel

- (id)copyWithZone:(NSZone*)zone {
    id copy = [[[self class] alloc] init];
    return copy;
}

- (nonnull id<NSObject>)diffIdentifier {
    return self.twitter;
}
@end
