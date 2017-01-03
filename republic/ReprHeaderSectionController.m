//
//  ReprHeaderSectionController.m
//  republic
//
//  Created by Prabhat Godse on 1/2/17.
//  Copyright © 2017 Prabhat Godse. All rights reserved.
//

#import "ReprHeaderSectionController.h"
#import "SenatorFeedCellCollectionViewCell.h"

@interface ReprHeaderSectionController()
@property (nonatomic, strong) NSString *object;
@end

@implementation ReprHeaderSectionController

- (NSInteger)numberOfItems {
    return 1;
}

- (CGSize)sizeForItemAtIndex:(NSInteger)index {
    return CGSizeMake(self.collectionContext.containerSize.width, 56);
}

- (UICollectionViewCell*)cellForItemAtIndex:(NSInteger)index {
    SenatorFeedCellCollectionViewCell *cell = [self.collectionContext
                                               dequeueReusableCellOfClass:[SenatorFeedCellCollectionViewCell class]
                                               forSectionController:self
                                               atIndex:index];
    NSString *twitterId = self.object;
    cell.fullName = twitterId;
    
    return cell;
}

- (void)didUpdateToObject:(id)object {
    self.object = object;
}

- (void)didSelectItemAtIndex:(NSInteger)index {
    
}

@end
